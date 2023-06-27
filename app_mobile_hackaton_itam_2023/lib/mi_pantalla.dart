import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:developer';

class MiPantalla extends StatefulWidget {
  @override
  _MiPantallaState createState() => _MiPantallaState();
}

class _MiPantallaState extends State<MiPantalla> {
  bool toggleValue = false;
  bool isLoading = false;
  String responseData = '';

  void toggleChanged(bool value) async {
    setState(() {
      toggleValue = value;
      isLoading = true;
    });
    print(toggleValue);
    if (toggleValue) {
      try {
        final response = await http.get(Uri.parse(
            'http://148.205.56.10/api/v1/control/?action=turn_on&entity_id=switch.2gang_switch_l1'));
        log(response.body);
        if (response.statusCode == 200) {
          setState(() {
            responseData = response.body;
            isLoading = false;
          });
        } else {
          setState(() {
            responseData = 'Error: ${response.statusCode}';
            isLoading = false;
          });
        }
      } catch (error) {
        setState(() {
          responseData = 'Error de conexión';
          isLoading = false;
        });
      }
    } else {
      try {
        final response = await http.get(Uri.parse(
            'http://148.205.56.10/api/v1/control/?action=turn_off&entity_id=switch.2gang_switch_l1'));
        log(response.body);
        if (response.statusCode == 200) {
          setState(() {
            responseData = response.body;
            isLoading = false;
          });
        } else {
          setState(() {
            responseData = 'Error: ${response.statusCode}';
            isLoading = false;
          });
        }
      } catch (error) {
        setState(() {
          responseData = 'Error de conexión';
          isLoading = false;
        });
      }
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Control Lights'),
      ),
      body: Center(
        child: Padding(
          padding: const EdgeInsets.symmetric(horizontal: 20),
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Row(
                mainAxisAlignment: MainAxisAlignment.spaceBetween,
                children: [
                  const Text('Light Blue'),
                  Switch(
                    value: toggleValue,
                    onChanged: toggleChanged,
                  ),
                ],
              ),
              const SizedBox(height: 20.0),
              if (isLoading)
                const CircularProgressIndicator()
              else if (responseData.isNotEmpty)
                Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    const Text('Encrypted Message: '),
                    Text(responseData),
                  ],
                )
              else
                Text('Pulsa el toggle para realizar la petición'),
            ],
          ),
        ),
      ),
    );
  }
}
