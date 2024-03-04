UP Big Data
===========

Deploy Vitepress

```sh
cd classes
npm run build
ssh char 'rm -r www/classes'
scp -r .vitepress/dist char:www/classes
```

Or via sup

```sh
ssh sup 'rm -r www/classes'
scp -r .vitepress/dist sup:www/classes
ssh sup 'ssh char "rm -r www/classes"; scp -r www/classes char:www/classes'
```
