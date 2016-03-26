<html>
	<head>
		<title>My SiS Pal</title>
		<meta charset="utf-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1" />
		<!--[if lte IE 8]><script src="assets/js/ie/html5shiv.js"></script><![endif]-->
		<link rel="stylesheet" href="css/main.css" />
		<!--[if lte IE 8]><link rel="stylesheet" href="assets/css/ie8.css" /><![endif]-->
	</head>
	<body>
    <?php exec("python server.py"); ?>

    <article class="container box style3">
      <header>
        <h2>Welcome, <?php echo $_POST["user_name"]; ?>!</h2>
      </header>
      <form method="post" action="index.php" name="loginform">
        <div class="row 50%">
          <div class="6u 12u$(mobile)"><input type="text" class="text" name="user_name" placeholder="Email" value="<?php echo $_POST['user_name'];?>"/></div>
          <div class="6u 12u$(mobile)"><input type="email" class="text" name="user_email" placeholder="Email" value="<?php echo $_POST['user_email'];?>"/></div>
          <div class="6u$ 12u$(mobile)"><input type="password" class="text" name="user_password" placeholder="Password" value="<?php echo $_POST['user_password'];?>" /></div>
          <div class="6u 12u$(mobile)"><input type="text" class="text" name="user_phone_number" placeholder="Phone Number" value="<?php echo $_POST['user_phone'];?>"/></div>
          <br>
          <div class="12u$">
            <ul class="actions">
              <li><input type="submit" value="Save" /></li>
            </ul>
          </div>
        </div>
      </form>
    </article>

		<!-- Scripts -->
			<script src="js/jquery.min.js"></script>
			<script src="js/jquery.scrolly.min.js"></script>
			<script src="js/jquery.poptrox.min.js"></script>
			<script src="js/skel.min.js"></script>
			<script src="js/util.js"></script>
			<script src="js/main.js"></script>

	</body>
</html>
