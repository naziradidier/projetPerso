
@extends('template')

@section('page_title')
Contactez-nous 
@endsection


@section('content')
    <form action="{{ route('contact.submit')}}" method="post">
        @csrf
        <div class="form-group">
            <label for="">Votre nom : </label>
            <input type="text" name="nom" class="form-control">
        </div>
        <div class="form-group">
            <label for="">Votre email : </label>
            <input type="text" name="email" class="form-control">
        </div>
        <div class="form-group">
            <label for="">Message : </label>
            <textarea name="message"  class="form-control" cols="30" rows="10"></textarea>
        </div>

        <button type="submit" class="btn btn-success">Envoyer </button>
    </form>
@stop