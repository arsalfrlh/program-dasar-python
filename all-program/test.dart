class Test {
  final String name;
  final String email;

  Test({required this.name, required this.email});
}

List<Test> testList = [
  Test(name: "Kwazaa", email: "kwanzaa@gmail.com"),
  Test(name: "Arsal", email: "arsal@gmail.com"),
  Test(name: "Fahrulloh", email: "fahrulloh@gmail.com"),
];

void main(){
  for(var data in testList){
    print("Nama User ${data.name}");
    print("Email User ${data.email}");
    print("\n");
  }
}