package agenda;

public class AgendaSemanal {

	// Criando um tipo enumerado

	enum DiasDaSemana {
		SUNDAY, MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY
	}

	private DiasDaSemana dia;
	private String horario;

	public AgendaSemanal(DiasDaSemana dia, String horario) {
		this.setDia(dia);
		this.setHorario(horario);
	}

	// getters e setters

	public DiasDaSemana getDia() {
		return dia;
	}

	private void setDia(DiasDaSemana dia) {
		this.dia = dia;
	}

	public String getHorario() {
		return horario;
	}

	private void setHorario(String horario) {
		this.horario = horario;
	}
}
