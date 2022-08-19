@extends('template')

@section('page_title', 'Nos spécialités')

@section('content')
    <div>Nombre de spécialité : {{ $count_specialite }}</div>

    <ul>
        @foreach ($specialites as $key => $specialite)
            <li><h3>{{ $specialite }} </h3></li>
        @endforeach
    </ul>   

@stop