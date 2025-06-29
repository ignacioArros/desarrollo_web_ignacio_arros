package springboot_app.springboot_app.controllers;

import springboot_app.springboot_app.models.Actividad;
import springboot_app.springboot_app.services.ActividadService;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/actividades")
public class ActividadController {
    private final ActividadService actividadService;

    public ActividadController(ActividadService actividadService) {
        this.actividadService = actividadService;
    }

    // Listar actividades finalizadas
    @GetMapping("/finalizadas")
    public List<Actividad> listarActividadesFinalizadas() {
        return actividadService.obtenerActividadesFinalizadas();
    }

}
