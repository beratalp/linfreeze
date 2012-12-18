#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, sys, shutil, getpass
print "Kullanıcınız kontrol ediliyor"
if getpass.getuser() == "root":
  pass
else:
  "Root değilsiniz"
  sys.exit()
print "LinFreeze konsol arayüzü"
sec1 = "1) Kur"
sec2 = "2) Kaldır"
sec3 = "3) Hakkında"
print sec1
print sec2
print sec3
sec = raw_input("Seçenek giriniz: ")
if sec == "1":
  print "LinFreeze kurulumu"
  print "Bu betik LinFreeze' i kuracak ve yapılandıracaktır"
  kad = raw_input("Dondurulacak kullanıcı adı: ")
  print "Kullanıcı adınız denetleniyor..."
  import os
  lista = os.listdir("/home")
  if kad in lista:
    pass
  else:
    print "Kullanıcı adınız hatalı"
    sys.exit()
  print "Doğrulama başarılı"
  onay = raw_input("Devam etmek istiyor musunuz? (e/h): ")
  if onay == "h":
    print "Çıkılıyor..."
    sys.exit()
  else:
    print "Devam ediliyor..."
  print "Yapılandırmanız kaydediliyor..."
  os.system("cp -R /home/%s/ /root" %kad)
  print "Yapılandırma dizinine yetkileriniz veriliyor..."
  os.system("chown -R %s:%s /root/%s" %(kad, kad, kad))
  print "Açılış yapılandırmanız yapılıyor"
  os.mkdir("/usr/share/linfreeze")
  shutil.copy("/etc/conf.d/local.start","/usr/share/linfreeze")
  dosya = open("/etc/conf.d/local.start","a")
  dosya.write("rsync –del -av /root/%s/ /home/%s/"%(kad, kad))
  print "İşlem bitti"
  isl = raw_input("Yeniden başlatılın mı (e/h): ")
  if isl == "e":
    print "REBOOTING"
    os.system("reboot")
  else:
    print "Çıkılıyor"
    sys.exit()
if sec == "2":
  print "LinFreeze kaldırma sistemi"
  onay = raw_input("Devam etmek istiyor musunuz? (e/h): ")
  if onay == "h":
    print "Çıkılıyor"
    sys.exit()
  else:
    pass
  print "Eski yapılandırmanız siliniyor"
  os.remove("/etc/conf.d/local.start")
  print "Yedeklenmiş yapılandırmanız kopyalanıyor"
  shutil.copy("/usr/share/linfreeze/local.start","/etc/conf.d/")
  print "İşlem tamamlandı"
  print "Çıkılıyor..."
if sec == "3":
  print """
LinFreeze dondurma uygulaması
Sürüm 1.0
Arayüz henüz hazır değildir
Bu program GNU/GPLv2 lisansıyla lisanslanmıştır
Teşekkürler
@fortran
@YVZ_61
  """
  sys.exit()
else:
  print "Lütfen bir seçenek giriniz"
  sys.exit()
    
  
