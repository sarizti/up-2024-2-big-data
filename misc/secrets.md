Secrets
=======

Mysql
-----

```
santi:Est@34.123.212.94/up_2024_2_big_data
```

SSH
---

```
santi@34.123.212.94
```

keys: cp

```sql
create table up_users (user primary key, password, updated_at, last_access);
```

```sh
ids=(santi 0224604 0216980 0216229 0229386 0228431 0224767 0225509 0220279 0225118 0234847 0225512 0224260 0260523 0225511 0218797 0227412 0213663 0224679 0224764 0224758)
for i in ${ids[@]}
do
  p=$(htpasswd -nbm $i $i)
  let l="${#i}+1"
  t=$(date +%s)
  sqlite3 /var/www/db.sqlite "insert into up_users (user, password, updated_at) values ('$i', '${p:$l}', $t)
    on conflict do update set password=excluded.password, updated_at=excluded.updated_at;"
done
```

reset pwd

```php
<?php
$user = $_SERVER["AUTHENTICATE_USER"];
$isPost = $_SERVER["REQUEST_METHOD"] == "POST";

$fail = isset($_GET["fail"]);
$success = isset($_GET["success"]);
$show = isset($_GET["show"]) && $user == "santi";
$db = new SQLite3('/var/www/db.sqlite');
$t = time();

if ($isPost) {
    $s_user = $_POST["user"] ?? null;
    $s_pwd = $_POST["password"] ?? null;
    $loc = $_SERVER['PHP_SELF'];
    if ($s_user && $s_pwd && $s_user == $user) {
    	$p = escapeshellarg($s_pwd);
    	$p=substr(rtrim(`htpasswd -nbm $user $p`), strlen($user)+1);
	$stmt = $db->prepare("update up_users set password=:p, updated_at=:t where user=:u;");
        $stmt->bindValue(":p", $p, SQLITE3_TEXT);
        $stmt->bindValue(":t", $t, SQLITE3_INTEGER);
        $stmt->bindValue(":u", $user, SQLITE3_TEXT);
	if ($res = $stmt->execute()) {
            header("Location: https://s.arizti.mx$loc?success", true, 302);
	    die;
	}
    }
    header("Location: https://s.arizti.mx$loc?fail", true, 302);
    die;
}
$users = [];
if ($show) {
    $rs = $db->query("select user, updated_at, last_access from up_users;");
    while($row = $rs->fetchArray(SQLITE3_ASSOC)) {
	$users[] = $row;
    }
}
$stmt = $db->prepare("update up_users set last_access=:t where user=:u;");
$stmt->bindValue(":t", $t, SQLITE3_INTEGER);
$stmt->bindValue(":u", $user, SQLITE3_TEXT);
$res = $stmt->execute();
?>
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <title>Change Password</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/css/bootstrap.min.css" integrity="sha384-xOolHFLEh07PJGoPkLv1IbcEPTNtaed2xpHsD9ESMhqIYd0nLMwNLD69Npy4HI+N" crossorigin="anonymous">
    <script src="https://unpkg.com/vue@3/dist/vue.global.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/lodash.escaperegexp@4.1.2/index.min.js"></script>
    <style>
        html,
        body {
            height: 100%;
        }
        body {
            padding-top: 20px;
            background-color: #f5f5f5;
        }
        .form-signin {
            width: 100%;
            max-width: 330px;
            padding: 15px;
            margin: 0 auto;
        }
        .form-signin .checkbox {
            font-weight: 400;
        }
        .form-signin .form-control {
            position: relative;
            box-sizing: border-box;
            height: auto;
            padding: 10px;
            font-size: 16px;
        }
        .form-signin .form-control:focus {
            z-index: 2;
        }
        #u {
            margin-bottom: -1px;
            border-bottom-right-radius: 0;
            border-bottom-left-radius: 0;
        }
        #p1 {
            margin-bottom: -1px;
            border-top-left-radius: 0;
            border-top-right-radius: 0;
            border-bottom-right-radius: 0;
            border-bottom-left-radius: 0;
        }
        #p2 {
            margin-bottom: 10px;
            border-top-left-radius: 0;
            border-top-right-radius: 0;
        }
    </style>
</head>

<body class="text-center">
<div id="app">
<form class="form-signin" method="POST">
    <h1 class="h3 mb-3 font-weight-normal">Change Password</h1>
    <div v-if="success" class="alert alert-success" role="alert">Success!</div>
    <div v-if="fail" class="alert alert-warning" role="alert">Fail :(</div>
    <label for="u" class="sr-only">User</label>
    <input type="text" id="u" class="form-control" value="<?=$user?>" readonly name="user">
    <label for="p1" class="sr-only">New password</label>
    <input type="text" id="p1" class="form-control" placeholder="New password" required autofocus name="password" v-model="passwd">
    <label for="p2" class="sr-only">Confirm</label>
    <input type="text" id="p2" class="form-control" placeholder="Confirm" required :pattern="pat" title="Passwords must match">
    <button class="btn btn-lg btn-primary btn-block" type="submit">Save</button>
</form>
<table class="table" v-if="users.length > 0">
  <thead>
    <tr>
      <th scope="col">ID</th>
      <th scope="col">Updated At</th>
      <th scope="col">Last Access</th>
    </tr>
  </thead>
  <tbody>
    <tr v-for="u of users">
      <th scope="row">{{u.user}}</th>
      <td>{{getDate(u.updated_at)}}</td>
      <td>{{getDate(u.last_access)}}</td>
    </tr>
  </tbody>
</table> 
</div>
<script>
    const app = Vue.createApp({
        data() {
            return {
                passwd: '',
                success: <?=json_encode($success)?>,
		        fail: <?=json_encode($fail)?>,
                users: <?=json_encode($users)?>,
            };
        },
        computed: {
            pat: function() { return escapeRegExp(this.passwd)/*.slice(1,-1)*/; }
        },
	    methods: {
            getDate(t) {
                 return t ? new Intl.DateTimeFormat("es-MX", {dateStyle: "medium", timeStyle:"medium"}).format(new Date(t*1000)) : '';
            }
        }
    });

    app.mount('#app');
</script>
</body>
</html>
```
