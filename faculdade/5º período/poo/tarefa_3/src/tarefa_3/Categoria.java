package tarefa_3;

import java.util.ArrayList;

public class Categoria {

	private final String nome;
	private ArrayList<Item> itens = new ArrayList<Item>();

	public Categoria(String nome) {
		this.nome = nome;
	}

	public void AddItem(Item item) {
		itens.add(item);
	}

	public void RemoveItem(short index) {
		itens.remove(index);
	}

	public StringBuilder listaItens() {
		StringBuilder sb = new StringBuilder();
		sb.append("Categoria: " + this.nome);
		
		for (Item item : itens) {
			sb.append("\n" + item.getCodigo());
		}

		return sb;
	}
}
