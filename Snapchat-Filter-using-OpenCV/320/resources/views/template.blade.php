
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>@yield('page_title') | IT-DEV</title>

    <link rel="stylesheet" href="css/bootstrap.css">
</head>
<body>
    <nav class="navbar navbar-expand-sm navbar-dark bg-primary">
        <a class="navbar-brand" href="#">IT DEV</a>
        <button class="navbar-toggler d-lg-none" type="button" data-toggle="collapse" data-target="#collapsibleNavId" aria-controls="collapsibleNavId"
            aria-expanded="false" aria-label="Toggle navigation"></button>
        <div class="collapse navbar-collapse" id="collapsibleNavId">
            <ul class="navbar-nav mr-auto mt-2 mt-lg-0  ">
                <li class="nav-item active">
                    <a class="nav-link" href="{{ route('home') }}">Home <span class="sr-only">(current)</span></a>
                </li>
                <li class="nav-item active">
                    <a class="nav-link" href="{{ route('nosspecialite') }}">Nos spécialités</a>
                </li>
                <li class="nav-item active">
                    <a class="nav-link" href="{{ route('module') }}">Nos Modules de formation</a>
                </li>
                <li class="nav-item active">
                    <a class="nav-link" href="{{ route('contact') }}">Contactez-nous</a>
                </li>
            </ul>
        </div>
    </nav>
    <div class="container">
        <h1>@yield('page_title')</h1>

        
        @yield('content')



    </div>


    <footer class="mt-5" style="position: absolute;bottom : 5px; width : 100%; color : white; text-align:center; background-color : black; height: 50px">
        <h3>Pieds de page </h3>
    </footer>
</body>
</html>