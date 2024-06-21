package agenda;

public class Compromisso {

	private AgendaSemanal agenda;
	private String local;
	private String descricao;

	// Estou mudando o construtor para garantir a integridade dos dados
	// (Só vou conseguir criar a classe passando os parâmetros na hora da criação)
	public Compromisso(AgendaSemanal agenda, String descricao, String local) {

		this.setAgenda(agenda);
		this.setDescricao(descricao);
		this.setLocal(local);
	}

	// getters e setters ====================

	public String getLocal() {
		return local;
	}

	private void setLocal(String local) {
		this.local = local;
	}

	public String getDescricao() {
		return descricao;
	}

	private void setDescricao(String descricao) {
		this.descricao = descricao;
	}

	public AgendaSemanal getAgenda() {
		return agenda;
	}

	private void setAgenda(AgendaSemanal agenda) {
		this.agenda = agenda;
	}

	// Alterando o método 'toString' para mudar a forma de como a classe
	// 'Compromisso' é impressa
	public String toString() {
		return "Você tem um compromisso em " + agenda.getDia() + ", às: " + agenda.getHorario() + "\nDescricao: "
				+ descricao + "\nLocal: " + local + ".";
	}
}