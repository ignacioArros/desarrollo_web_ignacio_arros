package springboot_app.springboot_app.controllers;

import springboot_app.springboot_app.dto.ActividadDto;
import springboot_app.springboot_app.services.ActividadService;
import springboot_app.springboot_app.services.NotaService;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/actividades")
public class ActividadController {
    private final ActividadService actividadService;
    private final NotaService notaService;

    public ActividadController(ActividadService actividadService, NotaService notaService) {
        this.actividadService = actividadService;
        this.notaService = notaService;
    }

    // Listar actividades finalizadas
    @GetMapping("/finalizadas")
    public List<ActividadDto> listarActividadesFinalizadas() {
        return actividadService.obtenerActividadesFinalizadasConPromedio(notaService);
    }
}
