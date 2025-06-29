package springboot_app.springboot_app.controllers;

import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import springboot_app.springboot_app.models.Nota;
import springboot_app.springboot_app.services.NotaService;

@RestController
@RequestMapping("/api/notas")
public class NotaController {
    private final NotaService notaService;

    public NotaController(NotaService notaService) {
        this.notaService = notaService;
    }

    @PostMapping
    public ResponseEntity<?> agregarNota(@RequestBody Nota nota) {
        if (nota.getNota() < 1 || nota.getNota() > 7) {
            return ResponseEntity.badRequest().body("La nota debe estar entre 1 y 7");
        }
        notaService.agregarNota(nota);
        Double promedio = notaService.calcularPromedioPorActividad(nota.getActividadId());
        return ResponseEntity.ok(promedio != null ? promedio : "-");
    }
}
