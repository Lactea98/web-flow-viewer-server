from urllib.parse import urlparse

def getParsedUrl(request):
    line = request.split("\n")
    url = line[0].split(" ")[1]
    host = line[1].replace("Host: ", "")
    
    link = urlparse("http://" + host + url)

    return {
        "host" : link.netloc,
        "path" : link.path.split("/"),
        "query" : link.query
    }

def getParsedRefererUrl(request):
    lines = request.split("\n")
    for line in lines:
        if line.startswith("Referer:"):
            referer = line.split(" ")[1]
            parse = urlparse(referer)

            return {
                "host" : parse.netloc,
                "path" : parse.path.split("/"),
                "query" : parse.query
            }
    else:
        return {}

def getStateCode(response):
    line = response[ : response.find("\n")]
    state_code = line.split(" ")[1]
    color = ""

    if state_code[0] == "1" or state_code[0] == "2" or state_code[0] == "3":
        color = "green"
    elif state_code[0] == "4":
        color = "yellow"
    else:
        color = "red"
    
    return {"code" : state_code, "color" : color}

def getMimeType(response):
    content_type = {
        "json" : ["application/json", "text/json", "text/x-json"],
        "html" : ["text/html", "text/plain"],
        "xml" : ["application/xml", "application/xml-external-parsed-entity", "application/xml-dtd", "application/mathtml+xml", "application/xslt+xml"],
        "script" : ["text/javascript", "application/javascript"]
    }

    lines = response.split("\n")
    for line in lines:
        if line.startswith("Content-Type:"):
            content_type_keys = content_type.keys()
            for key in content_type_keys:
                for type in content_type[key]:
                    if line.find(type) != -1:
                        return key
                else:
                    break
            break
    
    return "no found"