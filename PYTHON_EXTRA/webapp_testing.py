import requests as req

method_list = ["GET", "POST", "PUT", "DELETE", "PATCH", "PUT","TRACE","test"]

for method in method_list:
    r = req.request(method,"https://arz.vision/")
    if method == "TRACE" and "TRACE / HTTP/1.1" in r.text:
        print("ok")
    print(method,r.status_code,r.reason)