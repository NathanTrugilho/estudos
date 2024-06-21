package agenda;

import agenda.AgendaSemanal.DiasDaSemana;

public class TestaCompromisso {

	public static void main(String[] args) {

		AgendaSemanal ag1 = new AgendaSemanal(DiasDaSemana.MONDAY, "19:30");
		Compromisso c1 = new Compromisso(ag1, "Vou jantar com a morena do cabelo cacheado", "Casa amarela");
		
		System.out.println(c1);
	}
}
