<?php
class Test{
    var $name;
    var $email;

    function __construct($userName, $userEmail){
        $this->name = $userName;
        $this->email = $userEmail;
    }
}

$userList = [
    new Test("Kwanzaa","kwanza@gmail.com"),
    new Test("Arsal","arsal@gmail.com"),
];

foreach($userList as $user){
    echo "Nama User {$user->name}";
    echo "Nama User {$user->email}";
    echo "\n";
}