/*
  Description : Review 하면서 icareMatch app 만들기
  Date        : 2024.09.9 Mon PM 04:00
  Author      : Forrest DongGeun Park. (PDG)
  Updates     : 
	  2024.09.9  by pdg
		  -  기본적인 틀 . 
      - home.dart 만들기 , stf 를 쳐서 statefull widget 생성
      1) widget build return 에 scafold 를 생성한후 appbar를 만든다

  Detail      : 
	  - Flutter Project Review 
*/

import 'package:flutter/material.dart';

class Home extends StatefulWidget {
  const Home({super.key});

  @override
  State<Home> createState() => _HomeState();
}

class _HomeState extends State<Home> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text("i-CareMatch"),
        foregroundColor: Colors.white,
        backgroundColor: Colors.black,
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            ElevatedButton(
              onPressed: () => _clickButton(),
              child: Text("Click"))
          ],
        ),
      ),
    );
  }

  // -----Functions 
  _clickButton(){
    print("clicked");
  }
}