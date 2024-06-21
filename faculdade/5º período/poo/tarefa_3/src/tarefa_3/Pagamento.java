package tarefa_3;

import java.util.Date;

public class Pagamento {
	private final EPagamento tipo;
	private final Date data;
	private final double valor;
	
	public Pagamento(EPagamento tipo, Date data, double valor) {
		this.tipo = tipo;
		this.data = data;
		this.valor = valor;
	}

	public EPagamento getTipo() {
		return tipo;
	}

	public Date getData() {
		return data;
	}

	public double getValor() {
		return valor;
	}

}
