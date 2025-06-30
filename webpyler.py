from http.server import SimpleHTTPRequestHandler, HTTPServer
from io import BytesIO
import os,sys, ssl

######### CONFIG VARIABLES ########
certfile="cert.pem"
keyfile="private.key"
hostname = "localhost"
port = 8080 



######## WEBPYLER BUILDER ########

#folder paths and parts for webpylation
root_dir = "./html"
parts_dir = "./parts"
part_list = []

# LOAD IN HTML PARTS
for root, subFolders, files in os.walk(parts_dir):
    for file in files:
        file_name, file_extension = os.path.splitext(file)
        
        full_path = os.path.join(root, file)
        partFile = open(full_path)
        tag = "<" + file_name + file_extension +  ">"
        part_list.append((full_path, os.path.splitext(full_path)[0].replace(root_dir, ""), partFile.read(), tag))
        partFile.close()

def get_content_type(request_file):
    if request_file == "/":
        return "text/html"
    filename, file_extension = os.path.splitext(request_file)

    match file_extension:

        case ".html":
            return "text/html"
        case ".css":
            return "text/css"
        case ".ico":
            return "image/x-icon"


def webpyle(html_page):
    for part in part_list:
        html_page = html_page.replace(part[3], part[2])
    return html_page




######## SERVER SIDE FUNCTIONALITY #########



def get_html_page(page_name) -> str:
    if page_name == "/":
        page_name = "index"
    # remove folder and extension for consistency in file reading
    page_name = page_name.replace("/", "")
    page_name = page_name.replace(".html", "")
    
    for root, subFolders, files in os.walk(root_dir):
        for file in files:
            
            file_name, file_extension = os.path.splitext(file)
            if file_extension != ".html":
                return ""
            elif ((page_name + ".html") == file):
                
                return read_html_page(root +"/"+ file)

def read_html_page(full_path) -> str:
    infile = open(full_path, 'r', encoding="utf-8")
    outputText = infile.read()
    infile.close()
    return outputText

class WebpylerServer(SimpleHTTPRequestHandler):
    def _send_html_response(self, content, content_type):
        try:
            self.send_response(200)
            self.send_header("Content-type", content_type)
            self.end_headers()
            self.wfile.write(content.encode("utf-8"))
        except:
            print("An error with the encoding probably")

    def write_default_to_header(self,content_type):
        self.send_response(200)
        self.send_header("Content-type", content_type)
        self.end_headers()
        with open(self.path[1:], 'rb') as file: 
            self.wfile.write(file.read())   

    def do_GET(self):
        #TODO add other file support instead of just skipping for html 
        html = get_html_page(self.path)
        content_type = get_content_type(self.path)
        if html == "":
            return
        else:
            match content_type:
                case "text/html":
                    self._send_html_response(webpyle(html), content_type)
                case _:
                    self.write_default_to_header(content_type)

webserver = HTTPServer((hostname, port), WebpylerServer)


#ssl configuration
sslctx = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
sslctx.check_hostname = False
sslctx.load_cert_chain(certfile, keyfile)


# setup ssl socket
webserver.socket = sslctx.wrap_socket(webserver.socket, server_side=True)

if __name__ == "__main__":
    print("Server started https://%s:%s" % (hostname, port))

    try:
        webserver.serve_forever()
    except KeyboardInterrupt:
        pass

    webserver.server_close()
    print("server closed")
