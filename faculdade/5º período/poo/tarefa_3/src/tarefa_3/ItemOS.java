package tarefa_3;

public class ItemOS {
	private int qtde;
	private double preco;
	private Item item;

	public ItemOS(int qtde, double preco, Item item) {
		this.qtde = qtde;
		this.preco = preco;
		this.item = item;
	}

	public int getQtde() {
		return qtde;
	}

	public void setQtde(int qtde) {
		this.qtde = qtde;
	}

	public double getPreco() {
		return preco;
	}

	public void setPreco(double preco) {
		this.preco = preco;
	}

	public Item getItem() {
		return item;
	}

	public void setItem(Item item) {
		this.item = item;
	}
	
	public double getTotal() {
		return (qtde * this.preco);
	}
}
