UP Big Data
===========

Deploy Vitepress

```sh
cd classes
npm run build
scp -r .vitepress/dist santi@34.123.212.94:dist
ssh santi@34.123.212.94
sudo rm -r /var/www/html/classes
sudo mv dist /var/www/html/classes
exit
```
