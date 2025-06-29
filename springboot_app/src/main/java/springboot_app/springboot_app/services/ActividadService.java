package springboot_app.springboot_app.services;

import springboot_app.springboot_app.models.Actividad;
import springboot_app.springboot_app.repositories.ActividadRepository;
import org.springframework.stereotype.Service;

import java.time.LocalDateTime;
import java.util.List;

@Service
public class ActividadService {
    private final ActividadRepository actividadRepository;

    public ActividadService(ActividadRepository actividadRepository) {
        this.actividadRepository = actividadRepository;
    }

    public List<Actividad> obtenerActividadesFinalizadas() {
        return actividadRepository.findByDiaHoraTerminoBefore(LocalDateTime.now());
    }

}
