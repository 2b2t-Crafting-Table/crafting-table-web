def main(url):
    """

    :return:
    """
    lmn = """<script src="https://browser.sentry-cdn.com/5.12.1/bundle.min.js" integrity="sha384-y+an4eARFKvjzOivf/Z7JtMJhaN6b+lLQ5oFbBbUwZNNVir39cYtkjW1r6Xjbxg3" crossorigin="anonymous"></script><script>Sentry.init({ dsn: 'https://cc66efd98ae3494790ac9689940f77e7@sentry.io/2635837' });</script>"""
    return f"""
<!DOCTYPE html>
<html>

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, shrink-to-fit=no">
    <title>CTBOT-WEB</title>
    <meta name="description" content="CRAFTING TABLE">
    <link rel="stylesheet" href="/assets/bootstrap/css/bootstrap.min.css?h=a56a757409412f7812f2fb24a73f0abb">
    <link rel="stylesheet" href="/assets/css/animate.min.css">
    <link rel="stylesheet" href="/assets/css/styles.min.css?h=a2f0fa503db4abc4b40be839b16e9239">
</head>

<body class="text-center" style="background-color: #23272A;">
    <h1 style="font-size: 45px;color: #FFFFFF;">Crafting Table BOT overview</h1><a class="btn btn-link active text-lowercase text-center text-sm-center text-md-center text-lg-center text-xl-center d-flex float-none visible" role="button" data-toggle="tooltip" data-bs-tooltip="" data-bs-hover-animate="pulse"
        id="login-btn" style="background-image: url(&quot;/assets/img/Discord-Logo+Wordmark-White.png?h=d546a1986006a42b59818f25cc8d8a03&quot;);width: 816px;height: 251px;font-size: 50px;color: #2C2F33;align-items: center;align-content: center;align-self: center;background-color: #7289DA;filter: brightness(100%);opacity: 1;background-size: auto;background-repeat: round;"
        title="Log in with discord" href="{url}"></a>
    <h1 class="text-center" style="color: #FFFFFF;"><br><strong>Login with Discord</strong><br><br></h1>
    <script src="/assets/js/jquery.min.js?h=83e266cb1712b47c265f77a8f9e18451"></script>
    <script src="/assets/bootstrap/js/bootstrap.min.js?h=e46528792882c54882f660b60936a0fc"></script>
    <script src="/assets/js/script.min.js?h=cd7e26c62c422ae4fd1b6151814a03ae"></script>
</body>

</html>
""" + lmn
