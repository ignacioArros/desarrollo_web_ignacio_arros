package springboot_app.springboot_app.services;

import springboot_app.springboot_app.models.Nota;
import springboot_app.springboot_app.repositories.NotaRepository;
import org.springframework.stereotype.Service;
import java.util.List;

@Service
public class NotaService {
    private final NotaRepository notaRepository;

    public NotaService(NotaRepository notaRepository) {
        this.notaRepository = notaRepository;
    }

    public Nota agregarNota(Nota nota) {
        return notaRepository.save(nota);
    }

    public List<Nota> obtenerNotasPorActividad(Integer actividadId) {
        return notaRepository.findByActividadId(actividadId);
    }

    // Ver si utilizar este metodo en el controlador
    public Double calcularPromedioPorActividad(Integer actividadId) {
        List<Nota> notas = obtenerNotasPorActividad(actividadId);
        if (notas.isEmpty()) return null;
        return notas.stream().mapToInt(Nota::getNota).average().orElse(0.0);
    }
}
