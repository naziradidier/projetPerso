@extends('template')

@section('page_title', 'Nos modules')

@section('content')
    

    <table class="table table-light">
        <thead>
            <th>#</th>
            <th>Nom du module</th>
        </thead>
        <tbody>
            @foreach ($modules as $k => $module ) 
                <tr>
                    <td>{{ $k }}</td>
                    <td>{{ $module }}</td>
                </tr>
            @endforeach
        </tbody>
    </table>

@stop