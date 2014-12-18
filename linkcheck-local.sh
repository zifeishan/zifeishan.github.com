echo "Checking dead links:"
# python -m SimpleHTTPServer 8888 & 2>&1 >/dev/null
# ps | grep "python -m SimpleHTTPServer 8888" | awk -F ' ' '{print $1}'
linkchecker http://localhost:8888/ --timeout 10 --check-extern
