package tarefa_3;

public class Cliente extends Pessoa {
	
	private boolean platinum = false;
	
	public Cliente(long cpf, String nome, long telefone, String email) {
		super(cpf, nome, telefone, email);
	}

	public boolean isPlatinum() {
		return platinum;
	}

	public void setPlatinum(boolean platinum) {
		this.platinum = platinum;
	}

}
