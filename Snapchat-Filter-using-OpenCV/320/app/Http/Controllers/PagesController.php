<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class PagesController extends Controller
{
    

    public function index()
    {
        return view('home');
    }

    
    public function displaySpecialite()
    {
        $page_title = "Nos spécialités";
        $specialites = [
            1 => 'Gestion et Management',
            2 => 'Marketing',
            3 => 'Informatique Dev',
            4 => 'Comptabilité et Finances',
            5 => 'Informatiquen RSI'
        ];

        $count_specialite = count($specialites);

        return view('specialite', [
                'specialites' => $specialites, 
                'page_title' => $page_title,
                'count_specialite' => $count_specialite
            ]);
    
    }

    public function module()
    {   

        $modules = ['INFO 250', 'INFO 253', 'INFO 320' , 'INFO 532'];


        return view('module', compact('modules'));
    }

}
