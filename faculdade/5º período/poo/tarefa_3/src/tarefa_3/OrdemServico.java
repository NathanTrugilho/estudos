package tarefa_3;

import java.util.ArrayList;
import java.util.Date;

public class OrdemServico {
	private static int contador = 0;
	private final int numero;
	private final Date data;
	private final int kmAtual;
	private String descricao;
	private Funcionario consultor;
	private final Cliente cliente;
	private Pagamento pagamento;
	private final Veiculo veiculo;
	private ArrayList<ItemOS> itens = new ArrayList<>();

	public OrdemServico(int numero, Date data, int kmAtual, String descricao, Funcionario consultor, Cliente cliente,
			Pagamento pagamento, Veiculo veiculo) {
		this.numero = numero;
		this.data = data;
		this.kmAtual = kmAtual;
		this.descricao = descricao;
		this.consultor = consultor;
		this.cliente = cliente;
		this.pagamento = pagamento;
		this.veiculo = veiculo;
		contador = contador + 1;
	}

	public void addItem(Item i, int qtde) {
		ItemOS itemOS = new ItemOS(qtde, i.getPreco(), i);
		itens.add(itemOS);
	}

	public double getTotalServicos() {
		double soma = 0;
		
		if(this.cliente.isPlatinum() == true)
			return soma;
		
		for (ItemOS i : itens) {
			if (i.getItem().getTipo() == ETipoItem.SERVICO)
				soma = soma + i.getTotal();
		}
		return soma;
	}
	
	public double getTotalPecas() {
		double soma = 0;
		for (ItemOS i : itens) {
			if (i.getItem().getTipo() == ETipoItem.PECA)
				soma = soma + i.getTotal();
		}
		return soma;
	}
	
	public double getTotalOS() {
		return getTotalPecas() + getTotalServicos();
	}
	
	public StringBuilder listaOS() {
		StringBuilder sb = new StringBuilder();
		
		
		return sb;
	}

}
