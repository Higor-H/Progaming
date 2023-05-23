import java.util.Scanner;
class conjuntoDeAtividades1 {
  public static void main(String[] args) {
    System.out.println("Hello world!");
  
   Scanner ent = new Scanner (System.in);

   //exercício I
    
    int NumeroI1,NI2,Soma;
    System.out.println("Exercício I");
    System.out.println("Digite dois números inteiros.");
    System.out.println("Digite o 1° número:");
    NumeroI1 = ent.nextInt();
    System.out.println("digite o 2° número:");
    NI2 = ent.nextInt();
    Soma = NumeroI1 + NI2;
    System.out.println("soma:" + Soma);
    
   //exercício II
    
    int n1,n2,n3,n4,m2;
    System.out.println("exercício II");
    System.out.println("escreva suas 4 notas.");
    System.out.println("nota 1:");
    n1 = ent.nextInt();
    System.out.println("nota 2:");
    n2 = ent.nextInt();
    System.out.println("nota 3:");
    n3 = ent.nextInt();
    System.out.println("nota 4:");
    n4 = ent.nextInt();
    m2 = (n1+n2+n3+n4)/4;
    System.out.println("Sua media:" + m2);

    //exercício III

    int m,c;
    System.out.println("exercício III");
    System.out.println("escreva o valor em metros:");
    m = ent.nextInt();
    c = m*100;
    System.out.println("valor em cm:"+c);

    //exercício IV

    double ac,A;
    System.out.println("exercício IV");
    System.out.println("Digite um raio de um circulo");
    ac = ent.nextDouble();
    A = (ac*ac)*3.14;
    System.out.println("a area do circulo é:" + A);

    //exercício V

    int md,aq,dm;
    System.out.println("exercício V");
    System.out.println("medida do lado do quadrado");
    md = ent.nextInt();
    aq = md*md;
    dm = aq*2;
    System.out.println("Area do quadado:"+aq);
    System.out.println("dobro da area do quadrado:"+dm);

    //exercício VI

    double f,g;
    System.out.println("exercício VI");
    System.out.println("escreva a temperatura em fahrenheit");
    f = ent.nextDouble();
    g =5 * ((f-32) / 9);
    System.out.println("temperatura em graus celcius:" +g);
  }
}