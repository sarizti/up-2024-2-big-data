UP Big Data
===========

Deploy Vitepress

```sh
cd classes
npm run build
gsutil -m rm -r gs://s.arizti.mx/classes
gsutil -m cp -r .vitepress/dist/** gs://s.arizti.mx/classes/
```
