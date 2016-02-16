# mitmdump-jsondump
Simple prototype of a mitmdump script which dumps request&amp;response data as json.  
Each request/response flow pair is written to a new line.

Usage: mitmdump -s "jsondump.py out.json"

Example Output after request in out.json:

```
$cat out.json | jq .
```
```javascript
{
  "response": {
    "headers": {
      "Content-Type": "text/plain; charset=utf-8",
      "Cache-Control": "max-age=300",
      "ETag": "\"4f42be1e08a5811db30ce75f6bcfc2effe9ba1ef\"",
      "Vary": "Authorization,Accept-Encoding",
      "X-Content-Type-Options": "nosniff",
      "Via": "1.1 varnish",
      "X-GitHub-Request-Id": "C71B4C14:0C20:F24A224:56C14E2D",
      "X-Served-By": "cache-jfk1137-JFK",
      "Access-Control-Allow-Origin": "*",
      "X-Frame-Options": "deny",
      "X-Cache-Hits": "1",
      "Content-Security-Policy": "default-src 'none'",
      "X-XSS-Protection": "1; mode=block",
      "Content-Length": "149",
      "Expires": "Tue, 16 Feb 2016 16:35:14 GMT",
      "X-Fastly-Request-ID": "aeffc0c0b1bd653a35d87f82ec2a593122f9f2b9",
      "Date": "Tue, 16 Feb 2016 16:30:14 GMT",
      "Source-Age": "104",
      "X-Cache": "HIT",
      "Accept-Ranges": "bytes",
      "Strict-Transport-Security": "max-age=31536000",
      "Connection": "keep-alive"
    },
    "content": "# mitmdump-jsondump\nSimple prototype of a mitmdump script which dumps request&amp;response data as json.  \nUsage: mitmdump -s \"jsondump.py out.json\"\n"
  },
  "request": {
    "port": 443,
    "host": "raw.githubusercontent.com",
    "url": "https://raw.githubusercontent.com/sedand/mitmdump-jsondump/master/README.md"
  }
}
```
