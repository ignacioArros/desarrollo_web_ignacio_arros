package springboot_app.springboot_app.repositories;

import springboot_app.springboot_app.models.ActividadTema;
import org.springframework.data.jpa.repository.JpaRepository;
import java.util.List;

public interface ActividadTemaRepository extends JpaRepository<ActividadTema, Integer> {
    List<ActividadTema> findByActividadId(Integer actividadId);
}
