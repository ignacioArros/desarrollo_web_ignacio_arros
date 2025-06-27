package springboot_app.springboot_app.models;

import jakarta.persistence.*;

@Entity
@Table(name = "nota")
public class Nota {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Integer id;

    @Column(name = "actividad_id", nullable = false)
    private Integer actividadId;

    @Column(name = "nota", nullable = false)
    private Integer nota;

    // Getters y setters
    public Integer getId() {
         return id; 
    }

    public void setId(Integer id) {
         this.id = id; 
    }

    public Integer getActividadId() {
        return actividadId; 
    }

    public void setActividadId(Integer actividadId) {
        this.actividadId = actividadId;
    }

    public Integer getNota() {
        return nota; 
    }
    
    public void setNota(Integer nota) {
        this.nota = nota;
    }
}
