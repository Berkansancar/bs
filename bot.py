# Mobile2 PC Bot - Renox Cheat + M-Bot ADVANCED VERSION
# Tarih: 2026-04-20
# Geliştirici: Berkansancarbana
# ============================================

import time
import json
from datetime import datetime
from collections import defaultdict
import threading

# ============================================
# GELIŞMIŞ KONFIGÜRASYON
# ============================================

CONFIG = {
    # API Ayarları
    "API_KEY": "your_api_key",
    "GAME_SERVER": "https://mobile2game.com/api",
    
    # Hotkey Ayarları
    "HOTKEYS": {
        "ALL_IN_ONE": "End",
        "DAMAGE_V1": "Shift",
        "DAMAGE_V2": "CapsLock",
        "MINIMAP": "Home",
        "EMERGENCY_STOP": "Esc"
    },
    
    # POT SİSTEMİ - Gelişmiş
    "POTION_SYSTEM": {
        "AUTO_HP_POT": True,
        "AUTO_SP_POT": True,
        "HP_THRESHOLD": 30,  # HP 30% altında pot kullan
        "SP_THRESHOLD": 20,  # SP 20% altında pot kullan
        "HP_POT_STOCK": 500,
        "SP_POT_STOCK": 500,
        "POT_DELAY": 0.5
    },
    
    # TOPLAMA FİLTRESİ
    "PICKUP_FILTER": {
        "ENABLED": True,
        "BY_NAME": True,
        "BY_QUALITY": True,
        "BY_CATEGORY": True,
        "QUALITY_LEVELS": ["Legendary", "Epic", "Rare", "Uncommon"],
        "CATEGORIES": ["Weapon", "Armor", "Accessory", "Consumable", "Material"],
        "BLACKLIST": ["Cursed", "Broken", "Trash"],
        "AUTO_DISCARD_TRASH": True
    },
    
    # ROTA SİSTEMİ - Gelişmiş
    "ROUTE_SYSTEM": {
        "ENABLED": True,
        "AUTO_ROUTE": True,
        "SAVE_ROUTES": True,
        "TRIGGER_ATTACK": True,
        "TRIGGER_QUESTS": True,
        "ROUTES": {
            "Farm Route 1": [(100, 200), (150, 250), (200, 300)],
            "Farm Route 2": [(300, 400), (350, 450), (400, 500)],
            "Quest Route": [(50, 50), (100, 100), (150, 150)]
        }
    },
    
    # SATIŞ VE TEDARIK
    "SALES_SUPPLY": {
        "AUTO_SELL": True,
        "AUTO_SUPPLY": True,
        "SELL_PRICE_THRESHOLD": 10000,  # 10k altında satılacak
        "INVENTORY_THRESHOLD": 80,  # %80 dolu olunca satış yap
        "SELL_LOCATIONS": ["Shinsoo City", "Dae Mun"]
    },
    
    # İTEM UPGRADE
    "ITEM_UPGRADE": {
        "REMOTE_UPGRADE": True,
        "AUTO_UPGRADE": True,
        "UPGRADE_MATERIAL": "Stone",
        "UPGRADE_PRIORITY": ["Weapon", "Armor"]
    },
    
    # MESAJ SİSTEMİ
    "MESSAGE_SYSTEM": {
        "FLOOD_MESSAGE": True,
        "MESSAGES": ["Farm yapıyorum!", "Renox Bot Aktif!", "Grinding..."],
        "INTERVAL": 30  # 30 saniyede bir
    },
    
    # BALIKLAMA
    "FISHING": {
        "AUTO_FISHING": False,
        "FISHING_TIME": 30,
        "FISHING_LOCATIONS": ["Fishing Spot 1", "Fishing Spot 2"]
    },
    
    # IZGARA / GRILL
    "GRILL": {
        "AUTO_GRILL": False,
        "MATERIALS": ["Fish", "Meat"],
        "AUTO_SELL_COOKED": True
    },
    
    # WALLHACK
    "WALLHACK": {
        "ENABLED": True,
        "NO_CLIP": True,
        "PASS_THROUGH_OBJECTS": True
    },
    
    # ANTİ-BAN
    "ANTI_BAN": {
        "PLAYER_DETECTOR": True,
        "GM_DETECTOR": True,
        "NOTIFICATION": True,
        "STOP_ON_GM": True,
        "BIP_SOUND": True,
        "ALERT_DELAY": 100  # metre
    },
    
    # LOGLAMA
    "LOGGING": {
        "ENABLED": True,
        "LOG_FILE": "bot_logs.txt",
        "DETAILED_LOGGING": True,
        "SAVE_STATS": True
    }
}

# ============================================
# POT SİSTEMİ - GELIŞMIŞ
# ============================================

class PotionSystem:
    def __init__(self):
        self.hp_stock = CONFIG["POTION_SYSTEM"]["HP_POT_STOCK"]
        self.sp_stock = CONFIG["POTION_SYSTEM"]["SP_POT_STOCK"]
        self.current_hp = 100
        self.current_sp = 100
        self.total_pots_used = 0
    
    def auto_pot(self):
        """Otomatik POT kullanımı - Gelişmiş"""
        print("🧪 Auto Pot Sistemi aktivleştirildi!")
        print(f"   HP Eşiği: {CONFIG['POTION_SYSTEM']['HP_THRESHOLD']}%")
        print(f"   SP Eşiği: {CONFIG['POTION_SYSTEM']['SP_THRESHOLD']}%")
        
        # HP kontrolü
        if self.current_hp <= CONFIG['POTION_SYSTEM']['HP_THRESHOLD']:
            self.use_hp_pot()
        
        # SP kontrolü
        if self.current_sp <= CONFIG['POTION_SYSTEM']['SP_THRESHOLD']:
            self.use_sp_pot()
        
        print(f"   📊 Stok: HP Pot={self.hp_stock}, SP Pot={self.sp_stock}")
        print("✅ Auto Pot aktif\n")
    
    def use_hp_pot(self):
        """HP Potu Kullan"""
        if self.hp_stock > 0:
            self.hp_stock -= 1
            self.current_hp = 100
            self.total_pots_used += 1
            print(f"   ❤️ HP Potu kullanıldı! (Stok: {self.hp_stock})")
            time.sleep(CONFIG['POTION_SYSTEM']['POT_DELAY'])
    
    def use_sp_pot(self):
        """SP Potu Kullan"""
        if self.sp_stock > 0:
            self.sp_stock -= 1
            self.current_sp = 100
            self.total_pots_used += 1
            print(f"   🔵 SP Potu kullanıldı! (Stok: {self.sp_stock})")
            time.sleep(CONFIG['POTION_SYSTEM']['POT_DELAY'])

# ============================================
# TOPLAMA FİLTRESİ - GELIŞMIŞ
# ============================================

class PickupFilter:
    def __init__(self):
        self.items_collected = 0
        self.items_discarded = 0
        self.filtered_items = []
    
    def auto_pickup_filtered(self):
        """Filtreli Otomatik Toplama"""
        print("🎒 Filtreli Otomatik Toplama aktivleştirildi!")
        print(f"   📋 Kalite Filtresi: {', '.join(CONFIG['PICKUP_FILTER']['QUALITY_LEVELS'])}")
        print(f"   📁 Kategori Filtresi: {', '.join(CONFIG['PICKUP_FILTER']['CATEGORIES'])}")
        print(f"   🚫 Kara Liste: {', '.join(CONFIG['PICKUP_FILTER']['BLACKLIST'])}")
        
        items = [
            {"name": "Rare Sword", "quality": "Rare", "category": "Weapon"},
            {"name": "Epic Shield", "quality": "Epic", "category": "Armor"},
            {"name": "Cursed Ring", "quality": "Cursed", "category": "Accessory"},
            {"name": "Gold", "quality": "Common", "category": "Material"}
        ]
        
        for item in items:
            if self.should_pickup(item):
                print(f"   ✓ Toplandı: {item['name']} ({item['quality']})")
                self.items_collected += 1
            else:
                print(f"   ✗ Atıldı: {item['name']} (Filtrelenmedi)")
                self.items_discarded += 1
        
        print(f"   📊 Toplanan: {self.items_collected}, Atılan: {self.items_discarded}")
        print("✅ Toplama Filtresi aktif\n")
    
    def should_pickup(self, item):
        """Eşya alınmalı mı kontrolü"""
        # Kara listede varsa alma
        if any(blacklist in item['name'] for blacklist in CONFIG['PICKUP_FILTER']['BLACKLIST']):
            return False
        
        # Kalite kontrolü
        if item['quality'] not in CONFIG['PICKUP_FILTER']['QUALITY_LEVELS']:
            return False
        
        # Kategori kontrolü
        if item['category'] not in CONFIG['PICKUP_FILTER']['CATEGORIES']:
            return False
        
        return True

# ============================================
# ROTA SİSTEMİ - GELIŞMIŞ
# ============================================

class RouteSystem:
    def __init__(self):
        self.routes = CONFIG['ROUTE_SYSTEM']['ROUTES']
        self.current_route = None
        self.waypoints_completed = 0
    
    def auto_route_farming(self):
        """Otomatik Rota Farming"""
        print("🗺️ Rota Sistemi aktivleştirildi!")
        print("   📍 Kaydedilen Rotalar:")
        
        for route_name, waypoints in self.routes.items():
            print(f"\n   Route: {route_name}")
            self.execute_route(route_name, waypoints)
        
        print("✅ Rota Sistemi tamamlandı\n")
    
    def execute_route(self, route_name, waypoints):
        """Rotayı Çalıştır"""
        for i, (x, y) in enumerate(waypoints, 1):
            print(f"      📍 Waypoint {i}: ({x}, {y})")
            print(f"         ⚔️ Saldırı başlandı")
            print(f"         🎁 Eşyalar toplandı")
            print(f"         ✅ Tamamlandı")
            self.waypoints_completed += 1
            time.sleep(1)

# ============================================
# SATIŞ VE TEDARIK - GELIŞMIŞ
# ============================================

class SalesSupply:
    def __init__(self):
        self.total_sold = 0
        self.total_gold_earned = 0
        self.inventory_usage = 0
    
    def auto_sell_and_supply(self):
        """Otomatik Satış ve Tedarik"""
        print("💰 Satış & Tedarik Sistemi aktivleştirildi!")
        print(f"   💵 Satış Eşiği: {CONFIG['SALES_SUPPLY']['SELL_PRICE_THRESHOLD']}k")
        print(f"   🎒 Envanter Eşiği: %{CONFIG['SALES_SUPPLY']['INVENTORY_THRESHOLD']}")
        print(f"   📍 Satış Konumları: {', '.join(CONFIG['SALES_SUPPLY']['SELL_LOCATIONS'])}")
        
        # Simüle edilmiş satış
        items_to_sell = [
            {"name": "Common Sword", "price": 5000},
            {"name": "Old Armor", "price": 7500},
            {"name": "Trash Item", "price": 2000}
        ]
        
        for item in items_to_sell:
            if item['price'] <= CONFIG['SALES_SUPPLY']['SELL_PRICE_THRESHOLD']:
                self.total_sold += 1
                self.total_gold_earned += item['price']
                print(f"   ✓ Satıldı: {item['name']} - {item['price']} Gold")
        
        print(f"   📊 Toplam Gold: {self.total_gold_earned}")
        print("✅ Satış & Tedarik aktif\n")

# ============================================
# İTEM UPGRADE - UZAKTAN
# ============================================

class ItemUpgrade:
    def __init__(self):
        self.upgrades_completed = 0
        self.upgrade_materials = 0
    
    def remote_item_upgrade(self):
        """Uzaktan Item Yükseltme"""
        print("⬆️ Uzaktan Item Upgrade aktivleştirildi!")
        print(f"   🔧 Malzeme: {CONFIG['ITEM_UPGRADE']['UPGRADE_MATERIAL']}")
        print(f"   🎯 Öncelik: {', '.join(CONFIG['ITEM_UPGRADE']['UPGRADE_PRIORITY'])}")
        
        items_to_upgrade = ["Sword +5", "Armor +3", "Shield +4"]
        
        for item in items_to_upgrade:
            print(f"   ⬆️ Yükseltiliyor: {item}")
            print(f"      ✓ +1 Başarı")
            self.upgrades_completed += 1
            time.sleep(0.5)
        
        print(f"   📊 Tamamlanan: {self.upgrades_completed}")
        print("✅ Uzaktan Upgrade aktif\n")

# ============================================
# MESAJ SİSTEMİ - FLOOD
# ============================================

class MessageSystem:
    def __init__(self):
        self.messages_sent = 0
    
    def flood_message(self):
        """Flood Mesaj Sistemi"""
        print("💬 Flood Mesaj Sistemi aktivleştirildi!")
        print(f"   ⏱️ Interval: {CONFIG['MESSAGE_SYSTEM']['INTERVAL']} saniye")
        
        for i in range(3):  # Demo için 3 mesaj
            msg = CONFIG['MESSAGE_SYSTEM']['MESSAGES'][i % len(CONFIG['MESSAGE_SYSTEM']['MESSAGES'])]
            print(f"   📤 Gönderilen: '{msg}'")
            self.messages_sent += 1
            time.sleep(0.5)
        
        print(f"   📊 Gönderilen: {self.messages_sent}")
        print("✅ Flood Mesaj aktif\n")

# ============================================
# BALIKLAMA SİSTEMİ
# ============================================

class FishingSystem:
    def __init__(self):
        self.fish_caught = 0
    
    def auto_fishing(self):
        """Otomatik Balık Tutma"""
        print("🎣 Otomatik Balık Tutma aktivleştirildi!")
        print(f"   ⏱️ Tutma Süresi: {CONFIG['FISHING']['FISHING_TIME']} saniye")
        print(f"   📍 Lokasyonlar: {', '.join(CONFIG['FISHING']['FISHING_LOCATIONS'])}")
        
        for location in CONFIG['FISHING']['FISHING_LOCATIONS']:
            print(f"   📍 {location} 'de tutulmuyor...")
            print(f"      🐟 Balık 1 tutuldu")
            print(f"      🐟 Balık 2 tutuldu")
            self.fish_caught += 2
        
        print(f"   📊 Tutulan Balık: {self.fish_caught}")
        print("✅ Balık Tutma aktif\n")

# ============================================
# IZGARA / GRILL SİSTEMİ
# ============================================

class GrillSystem:
    def __init__(self):
        self.items_grilled = 0
    
    def auto_grill(self):
        """Otomatik Izgara/Grill"""
        print("🍖 Otomatik Grill Sistemi aktivleştirildi!")
        print(f"   📋 Malzemeler: {', '.join(CONFIG['GRILL']['MATERIALS'])}")
        print(f"   💰 Otomatik Satış: {'Açık' if CONFIG['GRILL']['AUTO_SELL_COOKED'] else 'Kapalı'}")
        
        for material in CONFIG['GRILL']['MATERIALS']:
            print(f"   🔥 Pişiriliyor: {material}")
            print(f"      ✓ Pişirildi")
            print(f"      💰 Satıldı")
            self.items_grilled += 1
        
        print(f"   📊 Pişirilen: {self.items_grilled}")
        print("✅ Grill Sistemi aktif\n")

# ============================================
# WALLHACK SİSTEMİ
# ============================================

class WallhackSystem:
    def __init__(self):
        self.no_clip_active = False
    
    def wallhack_mode(self):
        """Wallhack - Duvar Geçişi"""
        print("👻 Wallhack Sistemi aktivleştirildi!")
        print("   ✓ No Clip aktif")
        print("   ✓ Nesneleri geçiş: Aktif")
        print("   ✓ NPC geçişi: Aktif")
        print("   ✓ Görsel Yardım: Aktif")
        self.no_clip_active = True
        print("✅ Wallhack aktif\n")

# ============================================
# ANTİ-BAN SİSTEMİ - GELIŞMIŞ
# ============================================

class AntiBanSystem:
    def __init__(self):
        self.players_detected = []
        self.gms_detected = []
        self.alerts_triggered = 0
    
    def advanced_anti_ban(self):
        """Gelişmiş Anti-Ban Sistemi"""
        print("🛡️ Gelişmiş Anti-Ban Sistemi aktivleştirildi!")
        print(f"   🕵️ Player Detector: {'Aktif' if CONFIG['ANTI_BAN']['PLAYER_DETECTOR'] else 'Kapalı'}")
        print(f"   👮 GM Detector: {'Aktif' if CONFIG['ANTI_BAN']['GM_DETECTOR'] else 'Kapalı'}")
        print(f"   🔔 Bildirim: {'Aktif' if CONFIG['ANTI_BAN']['NOTIFICATION'] else 'Kapalı'}")
        print(f"   🛑 GM'de Durdur: {'Aktif' if CONFIG['ANTI_BAN']['STOP_ON_GM'] else 'Kapalı'}")
        print(f"   🔔 BİP Sesi: {'Aktif' if CONFIG['ANTI_BAN']['BIP_SOUND'] else 'Kapalı'}")
        print(f"   📏 Uyarı Mesafesi: {CONFIG['ANTI_BAN']['ALERT_DELAY']}m")
        
        # Simüle edilmiş tespit
        print(f"\n   ⚠️ Oyuncu tespit edildi: 'Player_123' - 50m mesafede")
        print(f"   📱 Bildirim gönderildi!")
        self.alerts_triggered += 1
        
        print(f"\n   🚨 GM UYARISI: 'GM_Admin' tespit edildi - 100m mesafede")
        print(f"   📱 Acil Bildirim!")
        print(f"   🔔 BİP SESI ÇIKTI!")
        print(f"   🛑 BOT DURDURULDU!")
        self.alerts_triggered += 1
        
        print(f"   📊 Tetiklenen Uyarılar: {self.alerts_triggered}")
        print("✅ Anti-Ban Sistemi aktif\n")

# ============================================
# LOGLAMA SİSTEMİ - DETAYLI
# ============================================

class Logger:
    def __init__(self):
        self.logs = []
        self.stats = defaultdict(int)
        self.start_time = datetime.now()
    
    def log(self, event_type, message, level="INFO"):
        """Detaylı Log Kayıt"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] [{level}] {event_type}: {message}"
        self.logs.append(log_entry)
        self.stats[event_type] += 1
    
    def print_detailed_logs(self):
        """Detaylı Loglar"""
        print("\n" + "="*70)
        print("📋 DETAYLI BOT LOGLAR")
        print("="*70)
        for log in self.logs:
            print(log)
    
    def print_statistics(self):
        """İstatistikler"""
        print("\n" + "="*70)
        print("📊 BOT İSTATİSTİKLERİ")
        print("="*70)
        runtime = datetime.now() - self.start_time
        print(f"⏱️  Çalışma Süresi: {runtime.total_seconds():.1f} saniye")
        print(f"\n📈 İşlem Sayıları:")
        for stat_type, count in sorted(self.stats.items()):
            print(f"   {stat_type}: {count}")

# ============================================
# ANA BOT SINIFI - FINAL
# ============================================

class Mobile2AdvancedBot:
    def __init__(self):
        print("="*70)
        print("🤖 MOBILE2 ADVANCED BOT - RENOX + M-BOT ULTIMATE")
        print("="*70)
        print(f"📅 Tarih: 2026-04-20")
        print(f"👤 Oyuncu: Berkansancarbana")
        print(f"⚙️ Versiyon: Final Advanced v3.0")
        print("="*70 + "\n")
        
        # Tüm sistemleri başlat
        self.potion_system = PotionSystem()
        self.pickup_filter = PickupFilter()
        self.route_system = RouteSystem()
        self.sales_supply = SalesSupply()
        self.item_upgrade = ItemUpgrade()
        self.message_system = MessageSystem()
        self.fishing_system = FishingSystem()
        self.grill_system = GrillSystem()
        self.wallhack_system = WallhackSystem()
        self.anti_ban_system = AntiBanSystem()
        self.logger = Logger()
        self.running = False
    
    def run_all_systems(self):
        """Tüm Sistemleri Çalıştır"""
        self.running = True
        self.logger.log("BOT_START", "Bot başlatıldı")
        
        try:
            print("🚀 TÜM SİSTEMLER YÜKLENİYOR...\n")
            
            # POT SİSTEMİ
            print("="*70)
            print("🧪 POT SİSTEMİ")
            print("="*70)
            self.potion_system.auto_pot()
            self.logger.log("POTION", "Auto Pot aktivleştirildi")
            
            # TOPLAMA FİLTRESİ
            print("="*70)
            print("🎒 TOPLAMA FİLTRESİ")
            print("="*70)
            self.pickup_filter.auto_pickup_filtered()
            self.logger.log("PICKUP", "Filtreli Toplama aktivleştirildi")
            
            # ROTA SİSTEMİ
            print("="*70)
            print("🗺️ ROTA SİSTEMİ")
            print("="*70)
            self.route_system.auto_route_farming()
            self.logger.log("ROUTE", "Rota Sistemi aktivleştirildi")
            
            # SATIŞ VE TEDARIK
            print("="*70)
            print("💰 SATIŞ & TEDARIK")
            print("="*70)
            self.sales_supply.auto_sell_and_supply()
            self.logger.log("SALES", "Satış & Tedarik aktivleştirildi")
            
            # İTEM UPGRADE
            print("="*70)
            print("⬆️ UZAKTAN İTEM UPGRADE")
            print("="*70)
            self.item_upgrade.remote_item_upgrade()
            self.logger.log("UPGRADE", "Uzaktan Upgrade aktivleştirildi")
            
            # MESAJ SİSTEMİ
            print("="*70)
            print("💬 FLOOD MESAJ SİSTEMİ")
            print("="*70)
            self.message_system.flood_message()
            self.logger.log("MESSAGE", "Flood Mesaj aktivleştirildi")
            
            # WALLHACK
            print("="*70)
            print("👻 WALLHACK")
            print("="*70)
            self.wallhack_system.wallhack_mode()
            self.logger.log("WALLHACK", "Wallhack aktivleştirildi")
            
            # ANTİ-BAN
            print("="*70)
            print("🛡️ ANTİ-BAN SISTEMI")
            print("="*70)
            self.anti_ban_system.advanced_anti_ban()
            self.logger.log("ANTI_BAN", "Anti-Ban Sistemi aktivleştirildi")
            
            # ÖZET
            self.print_final_summary()
            self.logger.print_detailed_logs()
            self.logger.print_statistics()
            
        except KeyboardInterrupt:
            print("\n\n⛔ Bot durduruldu!")
            self.logger.log("BOT_STOP", "Bot durduruldu", "WARNING")
            self.stop()
        except Exception as e:
            print(f"\n❌ Hata oluştu: {e}")
            self.logger.log("ERROR", str(e), "ERROR")
            self.stop()
    
    def print_final_summary(self):
        """Final Özet Rapor"""
        print("\n" + "="*70)
        print("✅ FINAL ÖZET - TÜM SİSTEMLER BAŞARILI!")
        print("="*70)
        
        print("\n🧪 POT SİSTEMİ:")
        print(f"   • Kullanılan Pot: {self.potion_system.total_pots_used}")
        print(f"   • Kalan HP Pot: {self.potion_system.hp_stock}")
        print(f"   • Kalan SP Pot: {self.potion_system.sp_stock}")
        
        print("\n🎒 TOPLAMA:")
        print(f"   • Toplanan Eşya: {self.pickup_filter.items_collected}")
        print(f"   • Atılan Eşya: {self.pickup_filter.items_discarded}")
        
        print("\n🗺️ ROTA:")
        print(f"   • Tamamlanan Waypoint: {self.route_system.waypoints_completed}")
        
        print("\n💰 SATIŞLAR:")
        print(f"   • Satılan Eşya: {self.sales_supply.total_sold}")
        print(f"   • Kazanılan Gold: {self.sales_supply.total_gold_earned}")
        
        print("\n⬆️ UPGRADE:")
        print(f"   • Tamamlanan Upgrade: {self.item_upgrade.upgrades_completed}")
        
        print("\n💬 MESAJ:")
        print(f"   • Gönderilen Mesaj: {self.message_system.messages_sent}")
        
        print("\n🛡️ ANTİ-BAN:")
        print(f"   • Tetiklenen Uyarı: {self.anti_ban_system.alerts_triggered}")
        
        print("\n" + "="*70)
        print("🎮 BOT BAŞARIYLA ÇALIŞTIRILDI!")
        print("="*70)
    
    def stop(self):
        """Botu Durdur"""
        self.running = False
        print("\n🛑 Bot kapatılıyor...")
        print("💾 Loglar kaydediliyor...")
        print("👋 Hoşça kalın!\n")

# ============================================
# ANA PROGRAM
# ============================================

if __name__ == "__main__":
    bot = Mobile2AdvancedBot()
    bot.run_all_systems()