<script setup lang="ts">
import {data} from './classes.data.ts'; 
//import {withBase} from "vitepress";
</script>
Info Para Clases
================

Website
: <https://s.arizti.mx/slides/clase1.html>

Classroom
: D-15

Classes
------

<pre>
{{data}}
</pre>

<ul>
<!--li v-for="cl of data">
<a :href="withBase(cl.url)">{{cl.title}}</a>
</li-->
</ul>
