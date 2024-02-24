UP Big Data
===========

Deploy Vitepress

```sh
cd classes
npm run build
ssh santiago@2806:2f0:5021:c949:8014:8a98:f70c:88ae 'rm -r www/classes'
scp -r .vitepress/dist 'santiago@[2806:2f0:5021:c949:8014:8a98:f70c:88ae]:www/classes'
scp -r www/classes 'santiago@[2806:2f0:5021:c949:8014:8a98:f70c:88ae]:www/classes'
```

santi@35.193.209.4 when in la up
