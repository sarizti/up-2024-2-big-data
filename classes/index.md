<script setup>
import {data} from './classes.data.js';

</script>
Info Para Clases
================

Website
: <https://s.arizti.mx/slides/clase1.html>

Classroom
: D-15

Classes
------

<ul>
<li v-for="cl of data">
<a :href="`/classes${cl.url}`">{{cl.frontmatter.title}}</a>
</li>
</ul>
