package tarefa_3;

import java.util.ArrayList;

public class Veiculo {
	private final String placa;
	private final int ano;
	private String cor;
	private Cliente proprietario;
	private final Modelo modelo;
	private ArrayList<OrdemServico> servicos = new ArrayList<>();

	public Veiculo(String placa, int ano, String cor, Cliente proprietario, Modelo modelo) {
		this.placa = placa;
		this.ano = ano;
		this.cor = cor;
		this.proprietario = proprietario;
		this.modelo = modelo;
	}

	public String getCor() {
		return cor;
	}

	public void setServicos(ArrayList<OrdemServico> servicos) {
		this.servicos = servicos;
	}

	public void setCor(String cor) {
		this.cor = cor;
	}

	public Cliente getProprietario() {
		return proprietario;
	}

	public void setProprietario(Cliente proprietario) {
		this.proprietario = proprietario;
	}

	public String getPlaca() {
		return placa;
	}

	public int getAno() {
		return ano;
	}

	public String getModelo() {
		return this.modelo.getNome();
	}
}
