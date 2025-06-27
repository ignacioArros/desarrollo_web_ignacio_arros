package springboot_app.springboot_app.repositories;

import springboot_app.springboot_app.models.Nota;
import org.springframework.data.jpa.repository.JpaRepository;
import java.util.List;

public interface NotaRepository extends JpaRepository<Nota, Integer> {
    List<Nota> findByActividadId(Integer actividadId);
}
