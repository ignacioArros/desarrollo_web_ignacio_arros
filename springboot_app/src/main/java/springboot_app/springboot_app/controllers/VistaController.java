package springboot_app.springboot_app.controllers;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class VistaController {

    @GetMapping("/")
    public String mostrarActividades() {
        return "notas";
    }
}
