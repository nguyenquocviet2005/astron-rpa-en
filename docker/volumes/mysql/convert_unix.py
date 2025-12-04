# Convert to Unix line endings (LF only)
content = open(r'e:\astron-rpa\docker\volumes\mysql\atoms_replace.sql', 'rb').read()

# Convert CRLF to LF
content = content.replace(b'\r\n', b'\n')

# Also convert any stray CR to LF
content = content.replace(b'\r', b'\n')

with open(r'e:\astron-rpa\docker\volumes\mysql\atoms_unix.sql', 'wb') as f:
    f.write(content)

print(f'Converted to Unix line endings: {len(content)} bytes')
print(f'LF count: {content.count(b"\\n")}')
