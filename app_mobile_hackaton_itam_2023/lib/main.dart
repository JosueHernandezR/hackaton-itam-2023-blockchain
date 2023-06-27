import 'package:flutter/material.dart';
import 'mi_pantalla.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Mi App',
      home: MiPantalla(),
    );
  }
}
