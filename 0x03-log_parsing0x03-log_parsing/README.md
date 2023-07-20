## LOG PARSInG

The solution about log parsing

ip_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
match = re.search(ip_pattern, text)
match.group()
