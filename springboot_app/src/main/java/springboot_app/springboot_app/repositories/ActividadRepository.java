package springboot_app.springboot_app.repositories;

import springboot_app.springboot_app.models.Actividad;
import org.springframework.data.jpa.repository.JpaRepository;
import java.time.LocalDateTime;
import java.util.List;

public interface ActividadRepository extends JpaRepository<Actividad, Integer> {
    // Para listar actividades finalizadas
    List<Actividad> findByDiaHoraTerminoBefore(LocalDateTime fechaActual);
}