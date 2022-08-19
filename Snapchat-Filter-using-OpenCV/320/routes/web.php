<?php

use Illuminate\Support\Facades\Route;
use App\Http\Controllers\PagesController;
use App\Http\Controllers\ContactsController;

/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| contains the "web" middleware group. Now create something great!
|
*/

Route::get('/',  [PagesController::class, 'index'])->name('home');
Route::get('specialite', [PagesController::class, 'displaySpecialite'])->name('nosspecialite');
Route::get('module', [PagesController::class, 'module'])->name('module');
Route::get('contact', [ContactsController::class, 'index'])->name('contact');

Route::post('submit-contact', [ContactsController::class, 'submitContact'])->name('contact.submit');