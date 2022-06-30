import requests,os,time

def tr():
	try:
		os.system("clear")
		requests.get("https://google.com/")
		print("[INFO] : ตอนนี้คุณเชื่อมต่ออินเทอร์เน็ตแล้ว !")
	except:
		os.system("clear")
		print("[INFO] : กรุณาเปิดอินเทอร์เน็ตก่อนใช้งาน !")



print("[INFO] : กำลังรออินเทอร์เน็ต...")
time.sleep(2)
tr()