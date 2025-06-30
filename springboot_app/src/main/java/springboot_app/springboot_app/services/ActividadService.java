package springboot_app.springboot_app.services;

import springboot_app.springboot_app.models.Actividad;
import springboot_app.springboot_app.repositories.ActividadRepository;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.List;
import java.time.LocalDateTime;
import java.util.Locale;

import springboot_app.springboot_app.dto.ActividadDto;

@Service
public class ActividadService {
    private final ActividadRepository actividadRepository;

    public ActividadService(ActividadRepository actividadRepository) {
        this.actividadRepository = actividadRepository;
    }

    public List<Actividad> obtenerActividadesFinalizadas() {
        return actividadRepository.findByDiaHoraTerminoBefore(LocalDateTime.now());
    }

    public List<ActividadDto> obtenerActividadesFinalizadasConPromedio(NotaService notaService) {
        List<Actividad> actividades = obtenerActividadesFinalizadas();
        List<ActividadDto> resultado = new ArrayList<>();
        for (Actividad act : actividades) {
            ActividadDto dto = new ActividadDto();
            dto.setId(act.getId());
            dto.setDiaHoraInicio(act.getDiaHoraInicio());
            dto.setSector(act.getSector());
            dto.setNombre(act.getNombre());
            dto.setTemas(act.getTemas());
            Double promedio = notaService.calcularPromedioPorActividad(act.getId());
            dto.setPromedioNotas(promedio != null ? String.format(Locale.US, "%.1f", promedio) : "-");
            resultado.add(dto);
        }
        return resultado;
    }

}
