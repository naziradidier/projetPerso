<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class ContactsController extends Controller
{
    public function index()
    {
        return view('contact');
    }

    public function submitContact()
    {
        dd($_POST);
    }
}
