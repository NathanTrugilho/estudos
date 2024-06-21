package tarefa_3;

public class Main {

	public static void main(String[] args) {
		
		Item i1 = new Item(ETipoItem.PECA, 1, "Porca tamanho 10", 0.60);
		Item i2 = new Item(ETipoItem.PECA, 2, "Porca tamanho 12", 0.70);
		Item i3 = new Item(ETipoItem.PECA, 3, "Porca tamanho 14", 0.80);
		
		Categoria c1 = new Categoria("Porcas");
		c1.AddItem(i1);
		c1.AddItem(i2);
		c1.AddItem(i3);
		
		System.out.println(c1.listaItens());
		
		ItemOS ios = new ItemOS(5, i1.getPreco(), i1);
		System.out.println(ios.getTotal());
		
		Cliente cl1 = new Cliente(123456, "Nathan", 2679, "nathan@email.com");
		Modelo m1 = new Modelo("Sedan");
		Veiculo v1 = new Veiculo("LRL", 2022, "Prata", cl1, m1);
		System.out.println(v1.getModelo());
	}

}
