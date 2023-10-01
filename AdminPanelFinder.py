#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
import time
import requests
import random
from bs4 import BeautifulSoup

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    banner = "\033[0;36m"
    banner += "╔═══╗─╔╗──────╔═══╗────────╔╗╔═══╗─────╔╗\n"
    banner += "║╔═╗║─║║──────║╔═╗║────────║║║╔══╝─────║║\n"
    banner += "║║─║╠═╝╠╗╔╦╦═╗║╚═╝╠══╦═╗╔══╣║║╚══╦╦═╗╔═╝╠══╦═╗\n"
    banner += "║╚═╝║╔╗║╚╝╠╣╔╗╣╔══╣╔╗║╔╗╣║═╣║║╔══╬╣╔╗╣╔╗║║═╣╔╝\n"
    banner += "║╔═╗║╚╝║║║║║║║║──║╔╗║║║║║═╣╚╣║──║║║║║╚╝║║═╣║\n"
    banner += "╚╝─╚╩══╩╩╩╩╩╝╚╩╝──╚╝╚╩╝╚╩══╩═╩╝──╚╩╝╚╩══╩══╩╝\n"
    banner += "\033[0m"
    print("\033[45mAuthor: coderfenrir\033[0m")
    print(banner)
    print("\033[42mÖrnek: https://example.com/\033[0m")
    print("\033[41mBazen Tam Sonuç Veremeyebilir.\033[0m")
    print("\033[0;33m==============================\033[0m")


def get_admin_panel(target_site):
    admin_panel_urls = [
        "admin/",
        "admin/login/",
        "admin/index/",
        "admin/home/",
        "admin/control/",
        "admin/panel/",
        "admin/dashboard/",
        "admin/console/",
        "admin/manage/",
        "admin/system/",
        "admin/configuration/",
        "admin/settings/",
        "admin/portal/",
        "admin/secure/",
        "admin/manager/",
        "admin/administrator/",
        "admin/login.php",
        "admin/index.php",
        "admin/home.php",
        "admin/control.php",
        "admin/panel.php",
        "admin/dashboard.php",
        "admin/console.php",
        "admin/manage.php",
        "admin/system.php",
        "admin/configuration.php",
        "admin/settings.php",
        "admin/portal.php",
        "admin/secure.php",
        "admin/manager.php",
        "admin/administrator.php",
        "admin/login.html",
        "admin/index.html",
        "admin/home.html",
        "admin/control.html",
        "admin/panel.html",
        "admin/dashboard.html",
        "admin/console.html",
        "admin/manage.html",
        "admin/system.html",
        "admin/configuration.html",
        "admin/settings.html",
        "admin/portal.html",
        "admin/secure.html",
        "admin/manager.html",
        "admin/administrator.html",
        "admin/login.asp",
        "admin/index.asp",
        "admin/home.asp",
        "admin/control.asp",
        "admin/panel.asp",
        "admin/dashboard.asp",
        "admin/console.asp",
        "admin/manage.asp",
        "admin/system.asp",
        "admin/configuration.asp",
        "admin/settings.asp",
        "admin/portal.asp",
        "admin/secure.asp",
        "admin/manager.asp",
        "admin/administrator.asp",
        "admin/login.aspx",
        "admin/index.aspx",
        "admin/home.aspx",
        "admin/control.aspx",
        "admin/panel.aspx",
        "admin/dashboard.aspx",
        "admin/console.aspx",
        "admin/manage.aspx",
        "admin/system.aspx",
        "admin/configuration.aspx",
        "admin/settings.aspx",
        "admin/portal.aspx",
        "admin/secure.aspx",
        "admin/manager.aspx",
        "admin/administrator.aspx",
        "system_administration/",
        "webadmin/index.html",
        "ss_vms_admin_sm/",
        "bb-admin/",
        "panel-administracion/",
        "instadmin/",
        "memberadmin/",
        "administratorlogin/",
        "adm.%EXT%",
        "admin_login.%EXT%",
        "panel-administracion/login.%EXT%",
        "pages/admin/admin-login.%EXT%",
        "pages/admin/",
        "acceso.%EXT%",
        "admincp/login.%EXT%",
        "admincp/",
        "adminarea/",
        "admincontrol/",
        "affiliate.%EXT%",
        "adm_auth.%EXT%",
        "memberadmin.%EXT%",
        "administratorlogin.%EXT%",
        "modules/admin/",
        "administrators.%EXT%",
        "siteadmin/",
        "siteadmin.%EXT%",
        "adminsite/",
        "kpanel/",
        "vorod/",
        "vorod.%EXT%",
        "adminpanel/",
        "PSUser/",
        "secure/",
        "webmaster/",
        "webmaster.%EXT%",
        "autologin.%EXT%",
        "userlogin.%EXT%",
        "admin_area.%EXT%",
        "cmsadmin.%EXT%",
        "security/",
        "usr/",
        "root/",
        "secret/",
        "admin/login.%EXT%",
        "admin/adminLogin.%EXT%",
        "moderator.php",
        "moderator.html",
        "moderator/login.%EXT%",
        "moderator/admin.%EXT%",
        "yonetici.%EXT%",
        "0admin/",
        "0manager/",
        "aadmin/",
        "cgi-bin/login%EXT%",
        "login1%EXT%",
        "login_admin/",
        "login_admin%EXT%",
        "login_out/",
        "login_out%EXT%",
        "login_user%EXT%",
        "loginerror/",
        "loginok/",
        "loginsave/",
        "loginsuper/",
        "loginsuper%EXT%",
        "login%EXT%",
        "logout/",
        "logout%EXT%",
        "secrets/",
        "super1/",
        "super1%EXT%",
        "super_index%EXT%",
        "super_login%EXT%",
        "supermanager%EXT%",
        "superman%EXT%",
        "superuser%EXT%",
        "supervise/",
        "supervise/Login%EXT%"
    ]

    admin_panel_url = None
    for url in admin_panel_urls:
        if "%EXT%" in url:
            extensions = ["php", "html", "asp", "aspx"]
            for ext in extensions:
                modified_url = url.replace("%EXT%", ext)
                full_url = target_site + modified_url
                response = requests.get(full_url)
                if response.status_code == 200:
                    admin_panel_url = full_url
                    break
        else:
            full_url = target_site + url
            response = requests.get(full_url)
            if response.status_code == 200:
                admin_panel_url = full_url
                break

    return admin_panel_url

def start_scanning():
    target_site = input("Hedef siteye girin: ")
    clear_screen()
    print_banner()
    print("\033[0;32mYönetici paneli taranıyor..\033[0m")
    time.sleep(5)
    admin_panel_url = get_admin_panel(target_site)
    if admin_panel_url:
        print(f"Yönetici paneli bulundu: {admin_panel_url}")
    else:
        print("\033[0;31mYönetici paneli bulunamadı.\033[0m")
    return admin_panel_url

def main():
    clear_screen()
    print_banner()
    print("\033[1;32m[01]\033[0m Başla")
    print("\033[1;31m[00]\033[0m Çıkış")

    choice = input("Seçiminizi girin: ")
    if choice == "01":
        admin_panel_url = start_scanning()
        while not admin_panel_url:
            choice = input("Taramaya devam edilsin mi? [Y/N]: ")
            if choice.lower() == "n":
                break
            admin_panel_url = start_scanning()
    elif choice == "00":
        print("\033[0;31mÇıkılıyor...\033[0m")
    else:
        print("Geçersiz seçim.")

if __name__ == "__main__":
    main()
